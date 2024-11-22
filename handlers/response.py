from rest_framework.response import Response

def custom_response(msg,data,error,status):    
    return Response({'msg' : msg ,"data":data,"error": error},status=status)
