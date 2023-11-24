import paho.mqtt.client as mqtt

# Define the MQTT broker hostname
broker = "test.mosquitto.org"

# Define the topics
topics = [
    "/rpi2023fall/+/red",
    "/rpi2023fall/+/green",
    "/rpi2023fall/+/yellow"
]

# Dictionary to store the status of lights
lights = {
    'red': 'off',
    'green': 'off',
    'yellow': 'off'
}

# Callback function when a message is received
def on_message(client, userdata, msg):
    topic_parts = msg.topic.split('/')
    color = topic_parts[-1]
    student_id = topic_parts[2]
    state = msg.payload.decode()

    # Update the status of the respective light
    lights[color] = state

    # Print the current status of lights
    print(f"Student ID: {student_id}")
    print(f"Red Light: {lights['red']}")
    print(f"Green Light: {lights['green']}")
    print(f"Yellow Light: {lights['yellow']}")
    print()

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to the topics
    for topic in topics:
        client.subscribe(topic)

# Initialize the MQTT client
client = mqtt.Client()

# Assign the on_connect and on_message functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, 1883, 60)

client.loop_forever()  # Start the MQTT loop
