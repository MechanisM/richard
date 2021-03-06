# richard -- video index system
# Copyright (C) 2012 richard contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.template.defaultfilters import slugify


class SiteNews(models.Model):
    """
    This is a really basic site news model. It's not designed to be
    WordPress. It is designed so it's easy to do site news on the site
    in the same style.
    """
    title = models.CharField(max_length=50)
    summary = models.TextField(help_text='Two sentences. Use HTML.')
    content = models.TextField(help_text='Use HTML.')
    # TODO: make this a django user instead?
    author = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True)

    class Meta(object):
        get_latest_by = "updated"
        ordering = ["-updated"]

    @models.permalink
    def get_absolute_url(self):
        return ('news', (self.pk, self.slug))

    def __unicode__(self):
        return '<SiteNews: %s>' % self.title

    def save(self):
        self.slug = slugify(self.title)
        super(SiteNews, self).save()
