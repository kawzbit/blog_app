from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefrq = "weekly"
    priority = 0.9

    def item(self):
        return Post.pulished.all()

    def lastmod(self, obj):
        return obj.updated
