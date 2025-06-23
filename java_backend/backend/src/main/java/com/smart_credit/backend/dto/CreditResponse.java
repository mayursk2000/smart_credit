package com.smart_credit.backend.dto;

import lombok.Data;
import java.util.Map;

@Data
public class CreditResponse {
    private double score;
    private Map<String, Double> explanation;
}
