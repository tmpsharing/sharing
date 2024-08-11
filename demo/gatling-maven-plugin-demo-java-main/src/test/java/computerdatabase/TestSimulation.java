package computerdatabase;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;

public class TestSimulation extends Simulation {
    HttpProtocolBuilder httpProtocol = http
            .baseUrl("http://localhost:8081")
            .acceptHeader("application/json");

    ChainBuilder getPj = exec(
            http("Home").get("/getHW").check(status().is(200)));


    ScenarioBuilder scn1 = scenario("Scenario 1").exec(getPj);

    {
        setUp(
//                scn1.injectOpen(constantUsersPerSec(300).during(10))
                scn1.injectClosed(constantConcurrentUsers(300).during(50))
        ).protocols(httpProtocol);
    }
}
