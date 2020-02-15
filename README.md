# django-performance-problem-solving
Practice based on https://medium.com/@hansonkd/performance-problems-in-the-django-orm-1f62b3d04785

# Unexpected Queries

        book = Book.objects.get(id=1)

        # -- Let's check the availability of
        # -- an author from Book model
        
        # --------------------------
        if book.author_id:
            print("passed with author_id without extra query")
        # --------------------------
        
        # --------------------------
        if book.author:
            print("passed with author with an extra query")
        # --------------------------