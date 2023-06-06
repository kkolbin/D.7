from django.contrib.auth.models import User
from .models import Author, Category, Post, Comment

# Создание пользователей
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создание объектов Author
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Добавление категорий
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Наука')

# Создание статей и новости
post1 = Post.objects.create(author=author1, post_type='article', title='Статья 1', content='Содержимое статьи 1', rating=0)
post2 = Post.objects.create(author=author2, post_type='article', title='Статья 2', content='Содержимое статьи 2', rating=0)
post3 = Post.objects.create(author=author1, post_type='news', title='Новость 1', content='Содержимое новости 1', rating=0)

# Добавление категорий к статьям/новости
post1.categories.add(category1, category2)
post2.categories.add(category3)
post3.categories.add(category4)

# Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий 1', rating=0)
comment2 = Comment.objects.create(post=post1, user=user2, text='Комментарий 2', rating=0)
comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий 3', rating=0)
comment4 = Comment.objects.create(post=post3, user=user2, text='Комментарий 4', rating=0)

# Изменение рейтингов объектов
post1.like()
post2.dislike()
comment1.like()
comment2.dislike()

# Обновление рейтингов авторов
author1.update_rating()
author2.update_rating()

# Вывод username и рейтинга лучшего пользователя
best_author = Author.objects.order_by('-rating').first()
print(best_author.user.username, best_author.rating)

# Вывод информации о лучшей статье
best_post = Post.objects.order_by('-rating').first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

# Вывод всех комментариев к лучшей статье
comments = Comment.objects.filter(post=best_post)
for comment in comments:
    print(comment.created_at, comment.user.username, comment.rating, comment.text)