from datamanager import RealTimeDataManager
import time

def clima(data):
	print(f"Datos en tiempo real actualizados: ",data)

real_time_data_manager = RealTimeDataManager()
real_time_data_manager.event_manager.subscribe( "clima", clima )




# Actualizaciones en tiempo real en segundo plano
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
        if real_time_data_manager.encontrar_cambio():
        	real_time_data_manager.notificar_cambio("clima", real_time_data_manager.data)
except KeyboardInterrupt:
    print("\nPrograma terminado.")




