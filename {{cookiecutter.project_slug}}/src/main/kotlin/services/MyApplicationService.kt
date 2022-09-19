package {{ cookiecutter.plugin_package }}.services

import {{ cookiecutter.plugin_package }}.MyBundle

class MyApplicationService {

    init {
        println(MyBundle.message("applicationService"))
    }
}
