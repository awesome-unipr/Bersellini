import paho.mqtt.client as mqtt
from aiohttp import web

class MqttClient:
    def __init__(self, host, port):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.host = host
        self.port = port

        self.mqtt_connection()

    def mqtt_connection(self):
        self.client.connect(self.host, self.port, 60)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
    
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print("Subscribed to " + topic)
    
    def publish(self,topic, message):
        self.client.publish(topic, message)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

class HttpServer:
    def __init__(self, radio_handler):
        self.app = web.Application()
        self.routes = web.RouteTableDef()

        self.radio_handler = radio_handler

        @self.routes.get('/radio')
        async def get_handler(request):
            station = self.radio_handler.display_station()
            return web.Response(text = station)

        @self.routes.post('/radio-change/')
        async def post_handler(request):
            data = await request.post()
            station = data['station']
            self.radio_handler.change_station(station)
            return web.Response(text = "Radio station has change to " + station)

        self.app.add_routes(self.routes)
    
    def start(self):
        web.run_app(self.app)
    
    def stop(self):
        web.run_app(self.app)

class RadioHandler:
    def __init__(self, default_station, mqtt_client):
        self._current_station = ""
        self._mqtt_client = mqtt_client
        self.change_station(default_station)
    
    def change_station(self, new_station):
        self._current_station = new_station
        self._mqtt_client.publish("vc2324/radio MQTT", "New station is " + new_station)
    
    def display_station(self):
        return self._current_station

mqtt_client = MqttClient('127.0.0.1', 1883)
radio_handler = RadioHandler("default_station", mqtt_client)
http_server = HttpServer(radio_handler)

mqtt_client.subscribe("vc2324/radio MQTT")
mqtt_client.start()

http_server.start()

mqtt_client.stop()

print("Program terminated!")