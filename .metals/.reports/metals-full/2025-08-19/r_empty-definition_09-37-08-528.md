error id: file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Simulations/BasicSimulation.scala:`<none>`.
file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Simulations/BasicSimulation.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -io/gatling/core/Predef.GetNextApi.
	 -io/gatling/core/Predef.GetNextApi#
	 -io/gatling/core/Predef.GetNextApi().
	 -io/gatling/http/Predef.GetNextApi.
	 -io/gatling/http/Predef.GetNextApi#
	 -io/gatling/http/Predef.GetNextApi().
	 -scala/concurrent/duration/GetNextApi.
	 -scala/concurrent/duration/GetNextApi#
	 -scala/concurrent/duration/GetNextApi().
	 -GetNextApi.
	 -GetNextApi#
	 -GetNextApi().
	 -scala/Predef.GetNextApi.
	 -scala/Predef.GetNextApi#
	 -scala/Predef.GetNextApi().
offset: 1711
uri: file:///C:/Users/ManikantaSanambatla/Downloads/gatling-maven-plugin-demo-main/gatling-maven-plugin-demo-main/src/test/scala/Simulations/BasicSimulation.scala
text:
```scala
package Simulations
import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BasicSimulation extends Simulation {
val users: Int = Integer.getInteger("USERS", 1)
val duration: Int = Integer.getInteger("DURATION", 1)
val httpProtocol = http
    .baseUrl("https://perf.invhub.fseng.net")
  val LoginRequest = scenario("Login and Extract Token")
    // 1. Send a POST request, save 'accessToken' as 'bearerToken'
    .exec(
      http("Login Request")
        .post("/v1/auth/apiLogin")
        .header("Content-Type", "application/json")
        .body(StringBody(
          """
          {
            "email": "perf-user-1@fseng.net",
            "apiKey": "bf8jBt3Zrjo9TLbNcy6H8t53K7J5r7"
          }
          """
        ))
        .asJson
        .check(jsonPath("$.accessToken").saveAs("bearerToken"))
    )
    // 2. Print the extracted bearerToken for user
    .exec { session =>
      println("Extracted bearerToken: " + session("bearerToken").asOption[String].getOrElse("NOT FOUND"))
      session
    }
    val GetNextApi = scenario("Get Next API")
    // 3. Send a GET request to the next API using the extracted bearerToken
    .exec(
      http("Get Next API")
        .get("/v1/queues/next")
        .header("Authorization", "Bearer ${bearerToken}")
        .check(status.is(200))
    )
    // 4. Print the response status for the next API
    .exec { session =>
      println("Response status for next API: " + session("responseStatus").asOption[Int].getOrElse("NOT FOUND"))
      session   
    }
  val scn=scenario("Basic Simulation")
    .exec(LoginRequest)
    .pause(1.second) // Pause for 1 second before the next request
    .exec(GetNextApi@@)
  setUp(
    scn.inject(
      rampUsers(users) during (duration.seconds)
    )
  ).protocols(httpProtocol)
}
```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.