from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text="Simple description text.")
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    
    class Meta:
        verbose_name = 'post' # 테이블의 별칭은 단수와 복수로 가질 수 있는데, 단수일 경우 'post'로 한다
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self): # 이 메소드가 정의된 객체를 지칭하는 url을 반환
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self): # get_previous_by_modify_dt는 장고의 내장 함수
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    
