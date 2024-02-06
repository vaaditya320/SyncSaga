# Create your views here.
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Story, StoryBranch
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Story

@login_required
def create_story(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description') 
        content = request.POST.get('content')

        # Create a new story
        new_story = Story.objects.create(
            title=title,
            description=description,
            content=content,
            author=request.user
        )

        messages.success(request, 'Story created successfully!')
        return redirect('dashboard')

    return render(request, 'create_story.html')

def view_stories(request):
    stories = Story.objects.all()
    context = {
        'stories': stories,
    }
    return render(request, 'view-story.html', context)

def view_story_detail(request, story_id):
    # Retrieve the story based on the provided ID
    story = get_object_or_404(Story, id=story_id)

    context = {
        'story': story,
    }

    return render(request, 'view-story-detail.html', context)


@login_required
def update_story_branch(request, story_id):
    original_story = get_object_or_404(Story, id=story_id)

    # Check if the current user is the owner of the original story
    is_owner = (request.user == original_story.author)

    if request.method == 'POST':
        if is_owner:
            # User A is updating their own story
            original_story.title = request.POST.get('title')
            original_story.description = request.POST.get('description')
            original_story.content = request.POST.get('content')
            original_story.save()
        else:
            # User B is creating a branch
            new_story_branch = StoryBranch(
                original_story=original_story,
                branched_by=request.user,
                modified_content=request.POST.get('content'),
            )
            new_story_branch.save()

            # Redirect to the view_story_changes page for the branch
            return redirect('view_story_changes', story_id=story_id)

        # Redirect to the view_story_detail page for the updated or branched story
        return redirect('view_story_detail', story_id=story_id)

    # Render the update-story-branch.html template with necessary context
    return render(request, 'update-story-branch.html', {'original_story': original_story, 'is_owner': is_owner})


@login_required
def view_story_changes(request, story_id):
    story = Story.objects.get(id=story_id)
    branches = StoryBranch.objects.filter(original_story=story)

    print("Story ID:", story.id)
    print("Story Title:", story.title)
    print("Number of Branches:", branches.count())

    context = {
        'story': story,
        'branches': branches,
    }

    return render(request, 'view-story-changes.html', context)