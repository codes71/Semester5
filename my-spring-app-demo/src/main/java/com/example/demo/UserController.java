package com.example.demo;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class UserController {

    @PostMapping("/login")
    public String authenticateUser(@RequestParam String username, @RequestParam String password) {
        if ("admin".equals(username) && "password".equals(password)) {
            return "Authenticated to admin";
        } else {
            return "Authentication Failed";
        }
    }
}