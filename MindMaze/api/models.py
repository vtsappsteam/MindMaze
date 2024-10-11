from django.db import models
import json

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    @classmethod
    def from_json(cls, json_data):
        """
        Class method to create a PDFDocument instance from a JSON string or dict.
        """
        if isinstance(json_data, str):
            try:
                json_data = json.loads(json_data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON string")
        
        # Get title and content from JSON data
        title = json_data.get('title', '')
        content = json_data.get('content', '')

        # Create a new instance of PDFDocument with the parsed data
        return cls(title=title, content=content)
