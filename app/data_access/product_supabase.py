# import the model class
from app.models.product import Product
from starlette.config import Config
from supabase import create_client, Client


# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)


# get all products
def dataGetProducts():
    response = supabase.table("product").select("*").execute()
    return response.data

# get product by id
def dataGetProduct(id):
    # select * from product where id = id 
    response = supabase.table("product").select("*").eq("id", id).execute()
    return response.data

#get all categories
def dataGetCategories():
    response=supabase.table("category").select("name").execute()
    return response.data

def dataAddProduct(product:Product):
    #id:40
    #titile:Laptop
    response=supabase.table("product").insert(product.dict()).execute()
    return response.data[0]

#update 

def dataUpdateProduct(product:Product,id):
    response=supabase.table("product").update(product.dict()).eq('id',id).execute()
    return response.data[0]

def dataDeleteProduct(id):
    response=supabase.table("product").delete().eq('id',id).execute()
    return response.data
