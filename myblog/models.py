from django.db import models

class Categroy(models.Model):
    #博客分类
    name = models.CharField('名字',max_length = 30)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name 

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField('名称',max_length = 16)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name 

    def __str__(self):
        return self.name 

class BlogPost(models.Model):
    title = models.CharField('标题',max_length = 50)
    author = models.CharField('作者',max_length = 16)
    content = models.TextField('内容',help_text = '博客内容')
    pub = models.DateField('发布时间',auto_now_add = True)
    email = models.EmailField('邮箱')
    categroy = models.ForeignKey(Categroy,verbose_name = '分类')
    tag = models.ManyToManyField(Tag,verbose_name = '标签')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name 

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost,verbose_name = '博客')
    name = models.CharField('称呼',max_length = 16)
    content = models.CharField('内容',max_length = 240)
    pub = models.DateField('发布时间',auto_now_add = True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name 

    def __str__(self):
        return self.content