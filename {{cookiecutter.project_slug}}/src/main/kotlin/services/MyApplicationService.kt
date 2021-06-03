package {{ cookiecutter.package_name }}.services

import {{ cookiecutter.package_name }}.MyBundle

class MyApplicationService {

    init {
        println(MyBundle.message("applicationService"))
    }
}
