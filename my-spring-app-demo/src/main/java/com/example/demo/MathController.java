package com.example.demo;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/math")
public class MathController {

    @GetMapping("/add")
    public String addNumbers(@RequestParam int a, @RequestParam int b) {
        int result = a + b;
        return "The sum of " + a + " and " + b + " is " + result;
    }
}