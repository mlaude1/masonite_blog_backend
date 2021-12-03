"""CreateBlogTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blog") as table:
            table.increments("id")
            table.string("title")
            table.string("body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blog")
