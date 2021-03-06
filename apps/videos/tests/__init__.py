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

from videos.models import CategoryKind, Category, Speaker, Tag, Video
from django.template.defaultfilters import slugify


def category_kind(**kwargs):
    defaults = {
        'name': 'foo'
        }
    defaults.update(kwargs)
    return CategoryKind(**defaults)


def category(**kwargs):
    defaults = {
        'name': 'Nameless category',
        'title': 'Nameless category 2012'
        }
    defaults.update(kwargs)
    if 'slug' not in defaults:
        defaults['slug'] = slugify(defaults['name'])
    if 'kind' not in defaults:
        ck = category_kind()
        ck.save()
        defaults['kind'] = ck
    return Category(**defaults)


def speaker(**kwargs):
    defaults = {
        'name': 'Ben Guaraldi'
        }
    defaults.update(kwargs)
    if 'slug' not in defaults:
        defaults['slug'] = slugify(defaults['name'])
    return Speaker(**defaults)


def tag(**kwargs):
    defaults = {
        'tag': 'tagless'
        }
    defaults.update(kwargs)
    return Tag(**defaults)


def video(**kwargs):
    defaults = {
        'title': 'How to build a video index site in 3 weeks',
        }
    defaults.update(kwargs)
    if 'category' not in defaults:
        cat = category()
        cat.save()
        defaults['category'] = cat
    return Video(**kwargs)
