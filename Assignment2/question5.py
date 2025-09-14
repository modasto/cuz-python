from abc import ABC, abstractmethod
import json
import pickle

class FileHandler(ABC):
    """Abstract Base Class for all file handlers"""
    
    def __init__(self, filename):
        self.filename = filename
        self.is_open = False
    
    @abstractmethod
    def read(self):
        """Read and return the contents of the file"""
        pass
    
    @abstractmethod
    def write(self, data):
        """Write data to the file"""
        pass
    
    def open(self):
        """Common method to mark file as open"""
        self.is_open = True
        print(f"Opened {self.filename}")
    
    def close(self):
        """Common method to mark file as closed"""
        self.is_open = False
        print(f"Closed {self.filename}")
    
    def __enter__(self):
        """Context manager support"""
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager support"""
        self.close()
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.filename})"


class TextFileHandler(FileHandler):
    """Concrete class for handling text files"""
    
    def read(self):
        """Read text file contents"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"Read {len(content)} characters from text file")
            return content
        except FileNotFoundError:
            print(f"Text file {self.filename} not found")
            return ""
        except Exception as e:
            print(f"Error reading text file: {e}")
            return ""
    
    def write(self, data):
        """Write data to text file"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(str(data))
            print(f"Wrote {len(str(data))} characters to text file")
            return True
        except Exception as e:
            print(f"Error writing to text file: {e}")
            return False


class BinaryFileHandler(FileHandler):
    """Concrete class for handling binary files"""
    
    def read(self):
        """Read binary file contents"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'rb') as file:
                content = file.read()
            print(f"Read {len(content)} bytes from binary file")
            return content
        except FileNotFoundError:
            print(f"Binary file {self.filename} not found")
            return b""
        except Exception as e:
            print(f"Error reading binary file: {e}")
            return b""
    
    def write(self, data):
        """Write data to binary file"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'wb') as file:
                if isinstance(data, (bytes, bytearray)):
                    file.write(data)
                else:
                    # Convert to bytes if not already
                    file.write(str(data).encode('utf-8'))
            print(f"Wrote data to binary file")
            return True
        except Exception as e:
            print(f"Error writing to binary file: {e}")
            return False


class JSONFileHandler(FileHandler):
    """Concrete class for handling JSON files"""
    
    def read(self):
        """Read and parse JSON file"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = json.load(file)
            print(f"Read JSON data from {self.filename}")
            return content
        except FileNotFoundError:
            print(f"JSON file {self.filename} not found")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON in {self.filename}")
            return {}
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return {}
    
    def write(self, data):
        """Write data as JSON to file"""
        if not self.is_open:
            self.open()
        
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)
            print(f"Wrote JSON data to {self.filename}")
            return True
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return False


# Demonstration
if __name__ == "__main__":
    print("=== File Handler System Demonstration ===\n")
    
    # Create different file handlers
    text_handler = TextFileHandler("example.txt")
    binary_handler = BinaryFileHandler("example.bin")
    json_handler = JSONFileHandler("data.json")
    
    handlers = [text_handler, binary_handler, json_handler]
    
    # Test writing with each handler
    print("=== Writing Files ===")
    sample_text = "Hello, World!\nThis is a text file."
    sample_binary = b"Binary\x00data\xFF\xFE"
    sample_json = {"name": "John", "age": 30, "city": "New York"}
    
    text_handler.write(sample_text)
    binary_handler.write(sample_binary)
    json_handler.write(sample_json)
    
    print("\n=== Reading Files ===")
    # Test reading with each handler
    text_content = text_handler.read()
    binary_content = binary_handler.read()
    json_content = json_handler.read()
    
    print(f"\nText content: {text_content!r}")
    print(f"Binary content: {binary_content!r}")
    print(f"JSON content: {json_content}")
    
    print("\n=== Polymorphism Demonstration ===")
    # Process all handlers uniformly
    for handler in handlers:
        print(f"\nUsing {handler}:")
        content = handler.read()
        print(f"Content type: {type(content).__name__}")
    
    print("\n=== Context Manager Demonstration ===")
    # Using context manager (with statement)
    with TextFileHandler("test.txt") as file:
        file.write("This was written using context manager!")
        content = file.read()
        print(f"Content: {content!r}")
    
    print("\n=== Error Handling ===")
    # Test with non-existent file
    missing_handler = TextFileHandler("nonexistent.txt")
    content = missing_handler.read()
    print(f"Content from missing file: {content!r}")
    
    print("\n=== Attempting to instantiate ABC directly (should fail) ===")
    try:
        # This should raise TypeError since FileHandler is abstract
        abstract_handler = FileHandler("test.txt")
    except TypeError as e:
        print(f"Error (expected): {e}")