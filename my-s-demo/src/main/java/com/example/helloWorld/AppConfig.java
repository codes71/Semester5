package com.example.helloWorld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AppConfig {
	@GetMapping("/hello")
	public String hello() {
		return "Hello World from Spring";
	}
}
