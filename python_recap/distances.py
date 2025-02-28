distances = {
    "Voyeger 1": 15200,
    "Voyeger 2": 12700,
    "New Horizons": 5200,
    "Cassini": 1400,
    "Juno": 500   
}
def main():
    for distance in distances.keys():
        print(f"{distance} is {convert(distances[distance])} km from Earth.")

def convert(au):
    return au * 1.0934
if __name__ == "__main__":
    main() 