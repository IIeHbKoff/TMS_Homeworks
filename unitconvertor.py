def inches_to_centimeters(x: [int, float]) -> float:
    return x * 2.54


def centimeters_to_inches(x: [int, float]) -> float:
    return x / 2.54


def miles_to_kilometers(x: [int, float]) -> float:
    return x * 1.609


def kilometers_to_miles(x: [int, float]) -> float:
    return x / 1.609


def pounds_to_kilograms(x: [int, float]) -> float:
    return x / 2.205


def kilograms_to_pounds(x: [int, float]) -> float:
    return x * 2.205


def grams_to_ounces(x: [int, float]) -> float:
    return x / 28.35


def ounces_to_grams(x: [int, float]) -> float:
    return x * 28.35


def gallons_to_liters(x: [int, float]) -> float:
    return x * 4.546


def liters_to_gallons(x: [int, float]) -> float:
    return x / 4.546


def pints_to_liters(x: [int, float]) -> float:
    return x / 1.76


def liters_to_pints(x: [int, float]) -> float:
    return x * 1.76


__all__ = [
    inches_to_centimeters, centimeters_to_inches, miles_to_kilometers, kilometers_to_miles,
    pounds_to_kilograms, kilograms_to_pounds, grams_to_ounces, ounces_to_grams, gallons_to_liters,
    liters_to_gallons, pints_to_liters, liters_to_pints
]
