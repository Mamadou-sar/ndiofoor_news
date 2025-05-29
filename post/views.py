from django.shortcuts import render

# Create your views here.
def get_posts(request):
    """
    View to get all posts.
    """
    # For now, we will just return an empty context
    context = {}

    # Render the 'list_posts.html' template with the context
    return render(request, 'post/list_posts.html', context)

def get_post(request, post_id):
    """  View to get a single post by ID.
    """
    # For now, we will just return an empty context
    context = {}
    return render(request, 'post/details_post.html', context)

def create_post(request):
    """
    View to create a new post.
    """
    # For now, we will just return an empty context
    context = {}
    
    # Render the 'create_post.html' template with the context
    return render(request, 'post/create_post.html', context)

def update_post(request, post_id):
    """
    View to update an existing post.
    """
    # For now, we will just return an empty context
    context = {}
    return render(request, 'post/update_post.html', context)

def delete_post(request, post_id):
    """  View to delete a post by ID.
    """  
    # For now, we will just return an empty context
    context = {}
    return render(request, 'post/delete_post.html', context)  