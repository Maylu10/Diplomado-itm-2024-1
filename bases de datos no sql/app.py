import boto3

#crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla_maira_cabezas')

#leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})

print(response['Item'])

#Leer todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])


tabla.put_item(Item={
    "id":"3",
    "nombre": "Maira Alejandra",
    "ciudad": "Medellin",
    "edad":32
})

#para Actualizar algun valor
response = tabla.get_item(Key={'id': '3'})

print("Elemento antes de actualizar", response['Item'])

response = table.update_item(
    Key={
        'id':'3'
    },
    updateExpression='SET edad = :val1' , #Expresion de actualizacion
    ExpressionAtributeValues={
        ':val1': 33 , # Nuevo valor para atributo1
        
    }
    
)
   
  #leer un elemento de la tabla
response = tabla.get_item(Key={'id': '3'})

print("Elemento despues de actualizar",response['Item'])

response = table.update_item(
    Key={
        'id':'3'
    },
    updateExpression='SET edad = :val1' , #Expresion de actualizacion
    ExpressionAtributeValues={
        ':val1': 32 , # Nuevo valor para atributo2
        
    }
    
)