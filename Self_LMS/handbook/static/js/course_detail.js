index = () => {
    console.log("courses_detail.js/index() STARSTSYT");
    const courseSlug = $("#course-detail").data("course-slug");
    const url = API.course.replace("COURSE_SLUG", courseSlug)
    console.log(courseSlug)
    // $(() => {
        
    // })
    $.get(url, (data) => {
        document.title = data.title;
        // console.log(data.chapters)
        console.log("API DATA:", data);
    console.log("Title:", data.title);
    console.log("Chapters:", data.chapters);
        chapterHTML = ""; sidebar = "";
        data.chapters.forEach(chapter => {
            const active = (chapter.slug === data.current_chapter ? "active" : "");

            chapterHTML += `
                <a href="/courses/${courseSlug}/${chapter.slug}/" class="list-group-item list-group-item-action">
                    <div class="d-flex justify-content-between align-items-start gap-3">
                        <div>
                            <div class="fw-semibold">${ chapter.title }</div>
                            <small class="text-muted">${ chapter.description }</small>
                        </div>
                        <i class="bi bi-chevron-right"></i>
                    </div>
                </a>
            `
            sidebar += `
                <a href="/courses/${courseSlug}/${chapter.slug}/"
                    class="list-group-item list-group-item-action ${active}">
                        ${chapter.title}
                </a>
            `
        });
        $("#sidebar_small_width").append(`${sidebar}` + `<a href="/course/${courseSlug}/start/" 
   class="list-group-item list-group-item-action">
    📝 Start Quiz
</a>`);
        $("#sidebar_big_width").append(`${sidebar}` + `<a href="/course/${courseSlug}/start/" 
   class="list-group-item list-group-item-action">
    📝 Start Quiz
</a>`);
        $("#course-detail").append(`
            <div class="mb-4">
                <a href="/courses/" class="btn btn-outline-secondary btn-sm mb-3">← My Courses</a>
                <h2 class="fw-bold mb-2">${data.title}</h2>
                <p class="text-muted mb-0">${ data.description }</p>
            </div>

            <div class="card shadow-sm border-0">
                <div class="card-body">
                    <div class="d-flex flex-wrap gap-2 mb-4">
                        <span class="badge bg-primary">${ data.level }</span>
                        <span class="badge bg-light text-dark">Duration: ${ data.duration }</span>
                    </div>

                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold mb-0">Course Content</h5>
                        <span class="badge bg-secondary">${ data.chapters.length } chapters</span>
                    </div>
                    <div class="list-group">
                        ${chapterHTML}
                    </div>
                </div>
            </div> 
            `)
    })
    


    
    console.log("courses_detail.js/index() END");
}



index()
/*
{% for chapter in data.chapters %}
                        <a href="{% url 'chapter_detail' data.slug chapter.slug %}" class="list-group-item list-group-item-action">
                            <div class="d-flex justify-content-between align-items-start gap-3">
                                <div>
                                    <div class="fw-semibold">${ chapter.title }</div>
                                    <small class="text-muted">${ chapter.description }</small>
                                </div>
                                <i class="bi bi-chevron-right"></i>
                            </div>
                        </a>
                        {% endfor %}
                        */