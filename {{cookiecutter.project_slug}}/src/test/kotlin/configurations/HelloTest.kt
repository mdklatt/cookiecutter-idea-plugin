/**
 * Unit tests for the Hello module.
 */
package {{ cookiecutter.plugin_package }}.configurations

import com.intellij.openapi.util.JDOMExternalizerUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import com.intellij.util.getOrCreate
import kotlin.test.assertNotNull
import kotlin.test.assertTrue
import org.jdom.Element
import org.junit.jupiter.api.Test


/**
 * Unit tests for the HelloConfigurationType class.
 */
class HelloConfigurationTypeTest {

    private var type = HelloConfigurationType()

    /**
     * Test the id property.
     */
    @Test
    fun testId() {
        assertTrue(type.id.isNotBlank())
    }

    /**
     * Test the icon property.
     */
    @Test
    fun testIcon() {
        assertNotNull(type.icon)
    }

    /**
     * Test the configurationTypeDescription property.
     */
    @Test
    fun testConfigurationTypeDescription() {
        assertTrue(type.configurationTypeDescription.isNotBlank())
    }

    /**
     * Test the displayName property.
     */
    @Test
    fun testDisplayName() {
        assertTrue(type.displayName.isNotBlank())
    }

    /**
     * Test the configurationFactories property.
     */
    @Test
    fun testConfigurationFactories() {
        type.configurationFactories.isNotEmpty()
    }
}


// The IDEA platform tests use JUnit3, so test class method names are used to 
// determine behavior instead of annotations. Notably, test classes are *not* 
// constructed before each test, so setUp() methods should be used for 
// per-test initialization where necessary. Also, test functions must be named 
// `testXXX` or they will not be found during automatic discovery.


/**
 * Unit tests for the HelloConfigurationFactory class.
 */
class HelloConfigurationFactoryTest : BasePlatformTestCase() {

    private lateinit var factory: HelloConfigurationFactory

    /**
     * Per-test initialization.
     */
    override fun setUp() {
        super.setUp()
        factory = HelloConfigurationFactory(HelloConfigurationType())
    }

    /**
     * Test the `id` property.
     */
    fun testId() {
        assertTrue(factory.id.isNotBlank())
    }

    /**
     * Test the `name` property.
     */
    fun testName() {
        assertTrue(factory.name.isNotBlank())
    }
}

/**
 * Unit tests for the HelloRunConfiguration class.
 */
class HelloRunConfigurationTest : BasePlatformTestCase() {

    private lateinit var factory: HelloConfigurationFactory
    private lateinit var config: HelloRunConfiguration

    /**
     * Per-test initialization.
     */
    override fun setUp() {
        super.setUp()
        factory = HelloConfigurationFactory(HelloConfigurationType())
        config = HelloRunConfiguration(project, factory, "Hello Test")
        return
    }

    /**
     * Test the constructor.
     */
    fun testConstructor() {
        assertEquals("World", config.subject)
        return
    }

    /**
     * Test round-trip write/read of settings.
     */
    fun testPersistence() {
        val element = Element("configuration")
        config.let {
            it.subject = "Foo"
            it.writeExternal(element)
        }
        HelloRunConfiguration(project, factory, "Persistence Test").let {
            it.readExternal(element)
            assertEquals(config.subject, it.subject)
        }
        return
    }
}


/**
 * Unit tests for the HelloSettingsEditor class.
 */
class HelloSettingsEditorTest : BasePlatformTestCase() {
    /**
     * Test the constructor.
     */
    fun testConstructor() {
        HelloSettingsEditor().apply {
            assertTrue(subject.isEmpty())
        }
        return
    }
}
