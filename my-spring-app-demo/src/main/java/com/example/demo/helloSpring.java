package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class helloSpring {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello";
    }
}