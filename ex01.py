import paho.mqtt.client as mqtt
import random
import time

# Define the MQTT broker hostnames
brokers = [
    "broker.hivemq.com",
    "broker.emqx.io",
    "test.mosquitto.org"
]

# Define the topics
topics = [
    "/rpi2023fall/[student_id]/red",
    "/rpi2023fall/[student_id]/green",
    "/rpi2023fall/[student_id]/yellow"
]

# Function to generate a random student ID
def generate_student_id():
    # Replace this with your student ID generation logic
    # For now, using a placeholder value
    return "S12345"

# Function to generate a random message
def generate_random_message():
    return random.choice(["on", "off"])

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Initialize the MQTT client
client = mqtt.Client()

# Assign the on_connect function
client.on_connect = on_connect

# Connect to a random broker
client.connect(random.choice(brokers), 1883, 60)

client.loop_start()  # Start the MQTT loop

while True:
    # Generate a random student ID
    student_id = generate_student_id()

    # Select a random topic
    topic = random.choice(topics).replace("[student_id]", student_id)

    # Generate a random message
    message = generate_random_message()

    # Publish the message to the selected topic
    client.publish(topic, message)
    print(f"Published to topic '{topic}': {message}")

    time.sleep(1)  # Wait for a short interval before publishing again
