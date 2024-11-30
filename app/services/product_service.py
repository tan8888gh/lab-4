from app.data_access.product_supabase import dataGetProducts, dataGetProduct,dataGetCategories,dataAddProduct,dataUpdateProduct,dataDeleteProduct
from app.models.product import Product
import json

# get list of products from data
def getAllProducts() :
    products = dataGetProducts()
    return products

def getProduct(id) :
    return dataGetProduct(id)

def getAllCategories():
    categories=dataGetCategories()
    return categories

def addNewProduct(product:Product):
    newProduct=dataAddProduct(product)
    return newProduct

def updateProduct(product:Product,id:int):
    updatedProduct=dataUpdateProduct(product,id)
    return updatedProduct

def deleteProduct(id:int):
    dataDeleteProduct(id)