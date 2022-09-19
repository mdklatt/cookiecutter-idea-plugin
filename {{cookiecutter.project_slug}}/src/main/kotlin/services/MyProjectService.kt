package {{ cookiecutter.plugin_package }}.services

import com.intellij.openapi.project.Project
import {{ cookiecutter.plugin_package }}.MyBundle

class MyProjectService(project: Project) {

    init {
        println(MyBundle.message("projectService", project.name))
    }
}
