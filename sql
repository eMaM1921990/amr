-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`areas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`areas` ;

CREATE TABLE IF NOT EXISTS `mydb`.`areas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `government` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`customers` ;

CREATE TABLE IF NOT EXISTS `mydb`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(255) NULL,
  `account_number` VARCHAR(45) NULL,
  `is_customer` TINYINT(1) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`items` ;

CREATE TABLE IF NOT EXISTS `mydb`.`items` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `price` DOUBLE NULL,
  `price_refactor` DOUBLE NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoice`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`invoice` ;

CREATE TABLE IF NOT EXISTS `mydb`.`invoice` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `invoice_date` DATETIME NULL,
  `area_id` INT NULL,
  `customer_id` INT NULL,
  `car_number` VARCHAR(45) NULL,
  `car_owner` INT NULL,
  `car_driver` VARCHAR(45) NULL,
  `created_by` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_invoice_1_idx` (`customer_id` ASC),
  INDEX `fk_invoice_2_idx` (`car_owner` ASC),
  INDEX `fk_invoice_3_idx` (`area_id` ASC),
  CONSTRAINT `fk_invoice_1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `mydb`.`customers` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_invoice_2`
    FOREIGN KEY (`car_owner`)
    REFERENCES `mydb`.`customers` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_invoice_3`
    FOREIGN KEY (`area_id`)
    REFERENCES `mydb`.`areas` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoice_line`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`invoice_line` ;

CREATE TABLE IF NOT EXISTS `mydb`.`invoice_line` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `item_id` INT NULL,
  `qantity` DOUBLE NULL,
  `invoice_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_invoice_line_1_idx` (`invoice_id` ASC),
  INDEX `fk_invoice_line_2_idx` (`item_id` ASC),
  CONSTRAINT `fk_invoice_line_1`
    FOREIGN KEY (`invoice_id`)
    REFERENCES `mydb`.`invoice` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_invoice_line_2`
    FOREIGN KEY (`item_id`)
    REFERENCES `mydb`.`items` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
