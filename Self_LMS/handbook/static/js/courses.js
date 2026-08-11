index = () => {
    console.log("courses.js/index() START");

    $(() => {
        $.get(API.cour, (data) => {
            data.forEach((course) => {
                let chaptersHtml = "";
                course.chapters.forEach((chapter) => {chaptersHtml += `
                    <li class="list-group-item px-0">
                        <i class="bi bi-journal-text me-2"></i>
                        <div>
                            <div class="fw-semibold">${ chapter.title }</div>
                            <small class="text-muted">${ chapter.description }</small>
                        </div>
                    </li>
                `})
                $("#course-list").append(`
                    <div class="col-md-6 col-xl-4">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">

                                <div class="d-flex justify-content-between align-items-start mb-3">
                                    <h5 class="card-title fw-bold mb-0">
                                        ${course.title}
                                    </h5>

                                    <div class="d-flex gap-2 flex-wrap">
                                        <span class="badge bg-primary">${course.level}</span>
                                    </div>
                                </div>

                                <p class="card-text text-muted">
                                    ${course.description}
                                </p>

                                <div class="mb-3 text-sm text-muted">
                                    <i class="bi bi-clock-history me-2"></i>
                                    ${course.duration}
                                </div>
                                <ul class="list-group list-group-flush">
                                    ${chaptersHtml}
                                </ul>
                                <div class="card-footer bg-white border-0 pt-0">
                                    <a href="/courses/${course.slug}/" class="btn btn-primary w-100">Open Course</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                `);
            });
        })
    })
    



    console.log("courses.js/index() END");
}



index()
/*
// <a href="{% url 'course_detail' ${course.slug} %}" class="btn btn-primary w-100">Open Course</a>'courses/<slug:course_slug>/'
                                <ul class="list-group list-group-flush">
                                    {% for chapter in course.chapters %}
                                    <li class="list-group-item px-0">
                                        <i class="bi bi-journal-text me-2"></i>
                                        <div>
                                            <div class="fw-semibold">{{ chapter.title }}</div>
                                            <small class="text-muted">{{ chapter.description }}</small>
                                        </div>
                                    </li>
                                    {% endfor %}
                                </ul>
                                <div class="card-footer bg-white border-0 pt-0">
                                    <a href="{% url 'course_detail' course.slug %}" class="btn btn-primary w-100">Open Course</a>
                                </div>
*/