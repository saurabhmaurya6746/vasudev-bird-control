from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "/",
            "/about/",
            "/contact/",
            "/blog/",
            "/gallery/",
            "/bird-netting-services/",
            "/bird-spike-system/",
            "/sport-net/",
            "/car-parking-net-system/",
            "/swimming-pool-protect-net-system/",
            "/safety-nets/",
            "/bird-netting-services-delhi/",
            "/bird-netting-services-prayagraj/",
            "/bird-netting-services-lucknow/",
            "/bird-netting-services-jaunpur/",
            "/bird-netting-services-varanasi/",
        ]

    def location(self, item):
        return item
