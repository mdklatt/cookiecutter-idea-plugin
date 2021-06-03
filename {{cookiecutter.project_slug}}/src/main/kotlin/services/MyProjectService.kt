package {{ cookiecutter.package_name }}.services

import com.intellij.openapi.project.Project
import {{ cookiecutter.package_name }}.MyBundle

class MyProjectService(project: Project) {

    init {
        println(MyBundle.message("projectService", project.name))
    }
}
