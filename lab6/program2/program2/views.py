from django.shortcuts import render, redirect

def first_page(request):
    if request.method == 'POST':
        # Store user input in Django session
        request.session['name'] = request.POST.get('name')
        request.session['roll'] = request.POST.get('roll')
        request.session['subject'] = request.POST.get('subject')

        # Redirect to second page
        return redirect('second_page')
    return render(request, 'firstPage.html')

def second_page(request):
    # Retrieve session data
    name = request.session.get('name', 'N/A')
    roll = request.session.get('roll', 'N/A')
    subject = request.session.get('subject', 'N/A')

    return render(request, 'secondPage.html', {'name': name, 'roll': roll, 'subject': subject})
