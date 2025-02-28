def main():
    sap = {"name": "Sap"}
    sap["age"] = 27
    sap.update({"school": "zap"})
    print(create(sap))


def create(sap):
    return f"""
    ============= Report =============
    Name: {sap.get("name","unkq")}
    Age: {sap["age"]}
    School: {sap.get("school","unknown")}
    ==================================
    """

if __name__ == "__main__":
    main()