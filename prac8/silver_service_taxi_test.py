from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("test taxi", 100, 2)
taxi.drive(10)
print(taxi)
print(f"${taxi.get_fare():.2f}")