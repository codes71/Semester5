package com.example.demo;


import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/register")
public class RegController {

    @PostMapping("/new")
    public String registerUser(@RequestParam String username, @RequestParam String password) {
        // Ideally, you would save this to a database
        return "User " + username + " registered successfully!";
    }
}