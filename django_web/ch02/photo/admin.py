from django.contrib import admin
from photo.models import Album, Photo

# 외래키로 연결된 Album, Photo 테이블 간에는 1:N 관계가 성립되므로, 앨범 객체를 보여줄 때 객체에 연결된 사진들을 같이 보여줄 수 있다.
# 같이 보여주는 형식은 StackedInline(세로) 또는 TabularInline(가로) 두 가지가 있다.
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2 # 이미 존재하는 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')