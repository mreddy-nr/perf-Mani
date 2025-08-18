error id: file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Engine.scala:`<none>`.
file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Engine.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -IDEPathHelper.
	 -scala/Predef.IDEPathHelper.
offset: 191
uri: file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Engine.scala
text:
```scala
import io.gatling.app.Gatling
import io.gatling.core.config.GatlingPropertiesBuilder

object Engine extends App {

	val props = new GatlingPropertiesBuilder()
		.resourcesDirectory(IDEPathHel@@per.mavenResourcesDirectory.toString)
		.resultsDirectory(IDEPathHelper.resultsDirectory.toString)
		.binariesDirectory(IDEPathHelper.mavenBinariesDirectory.toString)

	Gatling.fromMap(props.build)
}

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.