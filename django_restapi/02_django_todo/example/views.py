from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView # CBV
from rest_framework.decorators import api_view # FBV
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello World!")

# FBV
# /book/ 주소를 사용할 두 API에 대한 처리는 booksAPI()에서 한 번에 처리
@api_view(['GET', 'POST'])
def booksAPI(request): # /book/
    if request.method == 'GET':
        books = Book.objects.all() # Book모델로부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True) # 시리얼라이저에 전체 데이터를 한 번에 집어넣기 (직렬화, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) # return Response!
    
    elif request.method == 'POST': # Post Request (도서 정보 등록)
        serializer = BookSerializer(data=request.data) # POST 요청으로 들어온 데이터를 시리얼라이저에 삽입
        if serializer.is_valid():
            serializer.save() # 역직렬화를 통해 저장. 모델시리얼라이저의 기본 create() 함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def bookAPI(request, bid): # /book/bid/
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book) # 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK)



# CBV
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs): # GET Method 처리 함수(전체 목록)
        return self.list(request, * args, **kwargs) # mixins.ListModelMixin과 연결
    def post(self, request, *args, **kwargs): # POST Method 처리 함수 (1권 등록)
        return self.create(request, *args, **kwargs) # mixins.CreateModelMixin과 연결
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'
    # django 기본 모델 pk가 아닌 bid를 pk로 사용하고 있으니 lookup_field로 설정한다.
    
    def get(self, request, *args, **kwargs): # GET Method
        return self.retrieve(request, *args, **kwargs) # connect mixins.RetrieveModelMixin
    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):  
        return self.destroy(request, *args, **kwargs)
    
        