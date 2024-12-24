import os
import random
import socket
from datetime import datetime
from bson import ObjectId

class GenerateMongoObjID():
    def  __init__(self):
        pass
    
    def get_machine_identifier(self):
        """Generate a machine identifier."""
        machine_name = socket.gethostname()
        return hash(machine_name) & 0xFFFFFF  # Use a hash of the machine name, keeping only the last 3 bytes

    def get_process_identifier(self):
        """Generate a process identifier."""
        pid = os.getpid()
        return pid & 0xFFFF  # Use the last 2 bytes of the process id

    def get_counter(self):
        """Generate a random counter for uniqueness."""
        return random.randint(0, 0xFFFFFF)  # Generate a random 3-byte counter

    def generate_custom_object_id(self):
        """Generate a custom ObjectId with enhanced uniqueness."""
        # Timestamp: current time in seconds since Unix epoch (4 bytes)
        timestamp = int(datetime.utcnow().timestamp())

        # Machine identifier: 3 bytes
        machine_identifier = self.get_machine_identifier()

        # Process identifier: 2 bytes
        process_identifier = self.get_process_identifier()

        # Counter: 3 bytes
        counter = self.get_counter()

        # Construct the ObjectId
        custom_id = (
            timestamp.to_bytes(4, byteorder='big') +
            machine_identifier.to_bytes(3, byteorder='big') +
            process_identifier.to_bytes(2, byteorder='big') +
            counter.to_bytes(3, byteorder='big')
        )

        return ObjectId(custom_id)
