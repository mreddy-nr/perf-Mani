package Simulations
import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BasicSimulation extends Simulation {
val httpProtocol = http
    .baseUrl("https://perf.invhub.fseng.net")

  val scn = scenario("Save and View Response Data")
    // 1. Send a POST request, save 'accessToken' as 'bearerToken'
    .exec(
      http("Post with JSON body")
        .post("v1/auth/apiLogin")
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
    // 2. Print the extracted bearerToken
    .exec { session =>
      println("Extracted bearerToken: " + session("bearerToken").asOption[String].getOrElse("NOT FOUND"))
      session
    }

  setUp(
    scn.inject(atOnceUsers(1))
  ).protocols(httpProtocol)
}
