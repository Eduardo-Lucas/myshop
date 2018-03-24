# import requests
#
# from shop.serializers import CategorySerializer
#
#
# def get_categories():
#     resp_cat = requests.get('http://127.0.0.1:8001/categories/', auth=('usesoft', 'password123'))
#     json = resp_cat.json()
#     print('JSON: '+str(json))
#     serializer = CategorySerializer(data=json)
#     print('serializer: '+str(serializer))
#     if serializer.is_valid():
#         api_categories = serializer.save()
#         return api_categories
#     else:
#         print('serializer not valid!')
