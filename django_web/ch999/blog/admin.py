from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # slug는 title 필드를 사용해 미리 채워지도록 한다
    
     # Post 테이블과 Tag 테이블이 ManyToMany 관계이므로, Tag 테이블의 관련 레코드를 한 번의 쿼리로 가져오기 위함. 
     # N:N 관계에서 쿼리 횟수를 줄여 성능을 높이고자 할 때 prefetch_related() 메소드를 사용한다.
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())