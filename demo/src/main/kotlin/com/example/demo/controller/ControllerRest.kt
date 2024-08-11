package com.example.demo.controller

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController
import java.util.concurrent.atomic.AtomicInteger

@RestController
class ControllerRest {

    var i = AtomicInteger(0)

    @GetMapping("/getHW")
    fun getHW(): String {
        val current = i.incrementAndGet()
        if (current % 100 == 0) {
            println(current)
        }
        return "Hello world"
    }
}