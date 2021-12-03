"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Dec 3", "body": "Went to a lit birthday party"})
        Blog.create({"title": "May 15", "body": "Took Sarah Shafer to chick-fil-a for a hot date"})
        Blog.create({"title": "March 1", "body": "Let the madness begin 🔥"})
