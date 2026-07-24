#pydantic is a Python classes that define the shape, types, and validation rules for your data. It is builtin in fast API and is used to define request and response models, ensuring that the data being sent and received adheres to the expected structure and types. Pydantic models are used to validate incoming request data, serialize outgoing response data, and provide clear documentation for your API endpoints.
from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel): # this PostBase scheme defines the common fields and validation rules for a blog post. It inherits from BaseModel, which is the base class provided by Pydantic for creating data models.
    title:str=Field(min_length=1,max_length=100)
    content:str=Field(min_length=1)
    author:str=Field(min_length=1,max_length=50)

class PostCreate(PostBase): #this postCreate scheme defines what we expect when creating a new post. It inherits from PostBase and adds any additional fields or validation rules specific to the creation of a post.
    pass  

class PostResponse(PostBase): #this PostResponse scheme defines what we expect when returning a post in a response. It inherits from PostBase and adds any additional fields or validation rules specific to the response of a post.
    id:int
    date_posted:str

    model_config=ConfigDict(from_attributes=True) #this model_config attribute is used to configure the behavior of the Pydantic model. In this case, it is set to from_attributes=True, which means that the model will be populated from attributes of an object rather than from a dictionary. This is useful when you want to create a Pydantic model from an ORM model or any other object that has attributes corresponding to the fields defined in the Pydantic model.