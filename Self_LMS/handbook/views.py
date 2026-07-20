from django.http import Http404
from django.shortcuts import render

COURSES = [
    {
        "slug": "ai-fundamentals",
        "title": "AI Fundamentals",
        "description": "Nền tảng về trí tuệ nhân tạo, cách sử dụng prompt và các khái niệm cơ bản.",
        "duration": "4 weeks",
        "level": "Beginner",
        "chapters": [
            {"title": "Chapter 1: Giới thiệu AI", "route": "c1"},
            {"title": "Chapter 2: Prompt Engineering", "route": "c2"},
            {"title": "Chapter 3: Cơ bản về mô hình", "route": "c3"},
        ],
    },
    {
        "slug": "python-for-ai",
        "title": "Python for AI",
        "description": "Học cách dùng Python để xây dựng các workflow AI đơn giản và hiệu quả.",
        "duration": "6 weeks",
        "level": "Intermediate",
        "chapters": [
            {"title": "Chapter 4: Python cơ bản", "route": "c4"},
            {"title": "Chapter 5: Xử lý dữ liệu", "route": "c5"},
            {"title": "Chapter 6: Ứng dụng AI", "route": "c6"},
        ],
    },
]


def home(req):
    return render(req, 'home.html')


def base(req):
    return render(req, 'base.html')


def courses(req):
    return render(req, 'courses.html', {"courses": COURSES})


def course_detail(req, course_slug):
    course = next((item for item in COURSES if item["slug"] == course_slug), None)
    if course is None:
        raise Http404("Course not found")
    return render(req, 'course_detail.html', {"course": course})


def c1(req):
    return render(req, 'docs/chap1.html', {
        "page": "c1"
    })


def c2(req):
    return render(req, 'docs/chap2.html', {
        "page": "c2"
    })


def c3(req):
    return render(req, 'docs/chap3.html', {
        "page": "c3"
    })


def c4(req):
    return render(req, 'docs/chap4.html', {
        "page": "c4"
    })


def c5(req):
    return render(req, 'docs/chap5.html', {
        "page": "c5"
    })


def c6(req):
    return render(req, 'docs/chap6.html', {
        "page": "c6"
    })
