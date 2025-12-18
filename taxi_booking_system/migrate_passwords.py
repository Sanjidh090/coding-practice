"""
Migration Script - Convert Plain Text Passwords to Hashed Passwords
Run this once to migrate existing data to the new secure format
"""

import os
import sys
import hashlib
import shutil
from datetime import datetime

# Add the taxi_booking_system directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def hash_password(password: str) -> str:
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def is_password_hashed(password: str) -> bool:
    """Check if password is already hashed (SHA-256 produces 64 char hex string)"""
    return len(password) == 64 and all(c in '0123456789abcdef' for c in password.lower())


def migrate_file(filepath: str, password_index: int):
    """Migrate a data file to use hashed passwords"""
    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return 0
    
    # Create backup
    backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(filepath, backup_path)
    print(f"  Created backup: {backup_path}")
    
    # Read and process file
    migrated_count = 0
    lines = []
    
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split('|')
                if len(parts) > password_index:
                    password = parts[password_index]
                    if not is_password_hashed(password):
                        parts[password_index] = hash_password(password)
                        migrated_count += 1
                    lines.append('|'.join(parts) + '\n')
                else:
                    lines.append(line)
    
    # Write back
    with open(filepath, 'w') as f:
        f.writelines(lines)
    
    print(f"  Migrated {migrated_count} entries")
    return migrated_count


def main():
    """Main migration function"""
    print("="*70)
    print("  TAXI BOOKING SYSTEM - PASSWORD MIGRATION")
    print("="*70)
    print("\nThis script will convert all plain text passwords to secure hashed passwords.")
    print("A backup of each file will be created before migration.\n")
    
    response = input("Do you want to proceed? (yes/no): ").strip().lower()
    if response != 'yes':
        print("Migration cancelled.")
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    
    if not os.path.exists(data_dir):
        print(f"\nData directory not found: {data_dir}")
        print("Nothing to migrate.")
        return
    
    print("\nStarting migration...\n")
    
    total_migrated = 0
    
    # Migrate customers (password at index 2)
    print("Migrating customers.txt...")
    customers_file = os.path.join(data_dir, "customers.txt")
    total_migrated += migrate_file(customers_file, 2)
    
    # Migrate drivers (password at index 2)
    print("\nMigrating drivers.txt...")
    drivers_file = os.path.join(data_dir, "drivers.txt")
    total_migrated += migrate_file(drivers_file, 2)
    
    # Migrate administrators (password at index 2)
    print("\nMigrating administrators.txt...")
    admins_file = os.path.join(data_dir, "administrators.txt")
    total_migrated += migrate_file(admins_file, 2)
    
    print("\n" + "="*70)
    print(f"  MIGRATION COMPLETED - {total_migrated} passwords hashed")
    print("="*70)
    print("\n✅ All passwords have been securely hashed!")
    print("   Backup files have been created with .backup_* extension")
    print("   You can now safely use the GUI application.\n")


if __name__ == "__main__":
    main()
