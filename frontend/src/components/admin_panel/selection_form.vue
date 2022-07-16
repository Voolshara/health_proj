<template>
  <div v-if="!data['Selection']">У пацианта нет инсульта</div>
  <div v-else>
    <el-descriptions :column="1" border>
      <el-descriptions-item
        label="Дата Инсульта"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          this.data["Selection_dict"]["date_of_stroke"].split(" ")[1] +
          " " +
          this.data["Selection_dict"]["date_of_stroke"].split(" ")[2] +
          " " +
          this.data["Selection_dict"]["date_of_stroke"].split(" ")[3]
        }}</el-descriptions-item
      >
      <el-descriptions-item
        label="Вид Инсульта"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{ data["Selection_dict"]["type_of_stroke"] }}</el-descriptions-item
      >

      <el-descriptions-item
        label="Знает ли пользователь причину?"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{ data["Selection_dict"]["is_knew_reason"] }}</el-descriptions-item
      >

      <el-descriptions-item
        label="Проецент воспринимаемой информации"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          data["Selection_dict"]["percent_of_information"]
        }}%</el-descriptions-item
      >
      <el-descriptions-item></el-descriptions-item>

      <el-descriptions-item
        label="Имеется ли движения на поражённой ноге?"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          data["Selection_dict"]["is_injured_leg_movemented"]
        }}</el-descriptions-item
      >

      <div v-if="data['Selection_dict']['is_injured_leg_movemented'] == 'Да'">
        <el-descriptions-item
          label="На сколько % работает нога?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["percent_of_injured_leg_movemented"] }}%
        </el-descriptions-item>

        <el-descriptions-item
          label="Имеется ли у вас движения в голеностопе?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{
            data["Selection_dict"]["is_injured_ankle_movemented"]
          }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Может ли пациент сидеть без опоры под спину?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_can_sit"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Может ли пациент самостоятельно стоять?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_can_state"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Может ли пациент ходить с опорой?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{
            data["Selection_dict"]["is_patient_walk_with_supports"]
          }}</el-descriptions-item
        >
        <el-descriptions-item
          label="Сгибается ли нога в колленом суставе?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_knee_bend"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Имеются ли у вас движения на поражённой руке?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_knee_unbend"] }}</el-descriptions-item
        >
      </div>

      <el-descriptions-item></el-descriptions-item>
      <el-descriptions-item
        label="Имеются ли у вас движения на поражённой руке?"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          data["Selection_dict"]["is_injured_arm_movemented"]
        }}</el-descriptions-item
      >

      <div v-if="data['Selection_dict']['is_injured_arm_movemented'] == 'Да'">
        <el-descriptions-item
          label="На сколько % работает рука?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{
            data["Selection_dict"]["percent_of_injured_arm_movemented"]
          }}%</el-descriptions-item
        >

        <el-descriptions-item
          label="Сгибается ли рука в локтевом суставе?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_elbow_bend"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Разгибается ли рука в локтевом суставе?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_elbow_unbend"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Сгибается ли рука в предплечье?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{ data["Selection_dict"]["is_forearm_bend"] }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Разгибается  ли рука в предплечье?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{
            data["Selection_dict"]["is_forearm_unbend"]
          }}</el-descriptions-item
        >

        <el-descriptions-item
          label="Имеются ли у вас движения в пальцах на руке?"
          label-align="left"
          align="center"
          label-class-name="my-label"
          class-name="my-content"
          width="0"
          >{{
            data["Selection_dict"]["is_injured_finger_movemented"]
          }}</el-descriptions-item
        >
      </div>
      <el-descriptions-item></el-descriptions-item>

      <el-descriptions-item
        label="В каком году планируетe восстанавливаться?"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          data["Selection_dict"]["now_year_to_repair"]
            .replace("now", "В этом")
            .replace("later", "В последующих")
        }}</el-descriptions-item
      >

      <el-descriptions-item
        label="Где собираетесь восстанавливаться?"
        label-align="left"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
        width="0"
        >{{
          data["Selection_dict"]["where_to_repair"]
            .replace("outside", "За пределами страны")
            .replace("in_my_country", "В моей стране")
            .replace("home", "На дому")
        }}</el-descriptions-item
      >
    </el-descriptions>
  </div>
</template>

<script>
export default {
  name: "SelectionInPanel",
  props: {
    data: JSON,
  },
};
</script>
