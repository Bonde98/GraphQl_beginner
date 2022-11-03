import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Grocery

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','title')
        

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
                'id',
                'title',
                'author',
                'isbn',
                'pages',
                'price',
                'quantity',
                'description',
                'status',
                'date_created',
                )
        
class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageur1',
            'status',
            'date_created',
        )        
        
# Fournit le parametre de nos requets GraphQL
class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)
    
    
    # Pour ouvrir nos class, ils prennent deux parametre (root et info) 
    def resolve_books(root, info, **kwargs):
        return Book.objects.all()
    
    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()
    
    def resolve_groceries(root, info, **kwargs):
        return Grocery.objects.all()
    
# Apporte des donnes de notre type de (base de donnes)
schema = graphene.Schema(query=Query)

# Modifiction Categories 
class UpdateCategory(graphene.Mutation):
    # Argument: Nous permet de enregistrer des données dans la base de données
    class Arguments:
        # Mutation pour mettre à jour une catégorie
        title = graphene.String(required=True)
        id = graphene.ID()
    category = graphene.Field(CategoryType)
    
    
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)

# Créer Categories
class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        
    category = graphene.Field(CategoryType)
    
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)

#
class BookInput(graphene.InputObjectType):
   title = graphene.String()
   author = graphene.String()
   pages = graphene.Int()
   price = graphene.Int()
   quantity = graphene.Int()
   description = graphene.String()
   status = graphene.String()
   
# Création Livre
class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
    
    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        return CreateBook(book=book)
    
# Modifier Livre
class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()
        
    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.ge(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = input.price
        book.quantity = input.quantity
        book.save()
        return UpdateBook(book=book)


# Mutation qui définis nos mutations et envoies les parametre (creatin, mise à jour ...)
class Mutaton(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    
# Nous ajoutons une mutation à notre constructeur
schema = graphene.Schema(query=Query, mutation=Mutaton)