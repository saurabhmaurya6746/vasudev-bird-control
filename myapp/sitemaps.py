from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'index',
            'about',
            'contact',
            'bird-netting-services',
            'bird-spike-system',
            'bird-netting-services-delhi',
            'bird-netting-services-varanasi',
            'bird-netting-services-prayagraj',
            'bird-netting-services-lucknow',
            'bird-netting-services-jaunpur',
        ]

    def location(self, item):
        return reverse(item)
